slcpd is an auto-generated jupyter datascience notebook.

# Set Up Environment

Install `anaconda3` then,

```bash
conda env create -f ./environment.yml
source activate slcpd
```

# Load datasets

`python src/load_crime_data.py load_crime_data`

## Contribute

If you add new packages to the environment, save them with:

`conda env export -n coursera > environment.yml`

# Directory Structure

- develop # (Lab-notebook style)
  + [ISO 8601 date]-[DS-initials]-[2-4 word description].ipynb
  + 2017-06-28-fc-initial-data-clean.html
  + 2017-06-28-fc-initial-data-clean.ipynb
  + 2017-06-28-fc-initial-data-clean.py
  + 2017-07-02-dg-star-spectroscopy.html
  + 2017-07-02-dg-star-spectroscopy.pynb
  + 2017-07-02-dg-star-spectroscopy.py
- deliver # (final analysis, code, presentations, etc)
  + Star-Spectroscopy-Doppler-Shift.ipynb
  + Star-Spectroscopy-Doppler-Shift.html
  + Star-Spectroscopy-Doppler-Shift.py
- figures
  + 2017-07-16-dg-spectroscopy-human-spectrum.png
- src # (modules and scripts)
  + init.py
  + load_star_data.py
- data (backup-separate from version control)
  + spectroscopy-results.csv

# Set up script

https://gist.github.com/octaflop/aec9fdde899ef1646ca88243f775de00
