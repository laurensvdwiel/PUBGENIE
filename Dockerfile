FROM python:3.11-bookworm

EXPOSE 5000

# Download the file to the /app/data directory
RUN mkdir /data
# Kaplanis et al. 2020
RUN wget -P /data https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-020-2832-5/MediaObjects/41586_2020_2832_MOESM3_ESM.txt
# Satterstrom et al. 2020
RUN wget -P /data https://ars.els-cdn.com/content/image/1-s2.0-S0092867419313984-mmc1.xlsx

WORKDIR /app

RUN pip install --upgrade pip setuptools wheel

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app