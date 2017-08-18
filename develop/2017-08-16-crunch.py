
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
from pyproj import Proj, transform


# Set up our projections for the [Utah](http://www.spatialreference.org/ref/epsg/32043/) and [Web / GPS](http://www.spatialreference.org/ref/epsg/4326/) Projections

# In[33]:


# utah central
utc = Proj(init='epsg:32043', preserve_units=True)
gps = Proj(init='epsg:4326', preserve_units=True)
def convert_to_gps(row):
    x = row['x-coordinate']
    y = row['y-coordinate']
    return transform(utc, gps, x, y)


# ## 2016

# In[34]:


df_2016 = pd.read_csv('../data/slcpd_calls_2016.csv')


# In[35]:


df_2016.columns = map(str.lower, df_2016.columns)
df_2016.columns = map(str.strip, df_2016.columns)
df_2016.rename(columns={
    'x_coordinate': 'x-coordinate',
    'y_coordiante': 'y-coordinate',
    'city countil': 'city council'}, inplace=True)
df_2016.drop('time cleared', axis=1, inplace=True)
df_2016.drop('close type', axis=1, inplace=True)


# In[36]:


check_columns = df_2016.columns.tolist()
print(check_columns)


# In[37]:


df_2016['x_gps_coords'], df_2016['y_gps_coords'] = zip(*df_2016.apply(convert_to_gps, axis=1))


# In[38]:


master_columns = df_2016.columns.tolist()
print(master_columns)


# ## 2015

# In[39]:


df_2015 = pd.read_csv('../data/slcpd_calls_2015.csv')


# In[40]:


print(df_2015.columns)


# In[41]:


df_2015.columns = map(str.lower, df_2015.columns)
df_2015.columns = map(str.strip, df_2015.columns)
df_2015.rename(columns={
    'call number': 'case',
    'close as': 'close type',
    'call reason': 'call description',
    'x coordinate': 'x-coordinate',
    'y coordinate': 'y-coordinate'}, inplace=True)
df_2015.drop('close type', axis=1, inplace=True)


# In[42]:


checkset = set(check_columns)
df_2015set = set(df_2015.columns.tolist())
print(checkset.difference(df_2015set))
print(df_2015set.difference(checkset))


# In[43]:


df_2015['x_gps_coords'], df_2015['y_gps_coords'] = zip(*df_2015.apply(convert_to_gps, axis=1))


# ## 2014

# In[44]:


df_2014 = pd.read_csv('../data/slcpd_calls_2014.csv')


# In[45]:


print(check_columns)
print(df_2014.columns.tolist())


# In[48]:


df_2014.columns = map(str.lower, df_2014.columns)
df_2014.columns = map(str.strip, df_2014.columns)
df_2014.rename(columns={
    'call number': 'case',
    'close as': 'close type',
    'clear date': 'date cleared',
    'call reason': 'call description',
    'council': 'city council',
    'x coordinate': 'x-coordinate',
    'y coordinate': 'y-coordinate'}, inplace=True)
df_2014.drop('cleared description', axis=1, inplace=True)


# In[49]:


checkset = set(check_columns)
df_2014set = set(df_2014.columns.tolist())
print(checkset.difference(df_2014set))
print(df_2014set.difference(checkset))


# In[50]:


df_2014['x_gps_coords'], df_2014['y_gps_coords'] = zip(*df_2014.apply(convert_to_gps, axis=1))


# ## 2013

# In[51]:


df_2013 = pd.read_csv('../data/slcpd_calls_2013.csv')


# In[56]:


df_2013.columns = map(str.lower, df_2013.columns)
df_2013.columns = map(str.strip, df_2013.columns)
df_2013['time cleared'] = np.nan
df_2013.rename(columns={
    'clear date': 'date cleared',
    'call number': 'case',
    'close description': 'close type',
    'call reason': 'call description',
    'council': 'city council',
    'x coordinate': 'x-coordinate',
    'y coordinate': 'y-coordinate'}, inplace=True)
df_2013.drop('time cleared', axis=1, inplace=True)
df_2013.drop('close type', axis=1, inplace=True)


# In[57]:


checkset = set(check_columns)
df_2013set = set(df_2013.columns.tolist())
print(checkset.difference(df_2013set))
print(df_2013set.difference(checkset))


# In[58]:


df_2013['x_gps_coords'], df_2013['y_gps_coords'] = zip(*df_2013.apply(convert_to_gps, axis=1))


# In[59]:


df = pd.concat([df_2016, df_2015, df_2014, df_2013])


# In[60]:


df.index = df['case']


# In[61]:


df.tail()


# # Export

# In[ ]:


df.to_csv('../data/SLC_Police_Calls_2013__2016_cleaned_geocoded.csv')


# In[ ]:




