FROM public.ecr.aws/lambda/python:3.10
# Install chrome dependencies
RUN yum install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm jq unzip \
    && yum clean all

# Copy and run the chrome installer script
COPY ./chrome-installer.sh ./chrome-installer.sh
RUN chmod +x ./chrome-installer.sh
RUN ./chrome-installer.sh
RUN rm ./chrome-installer.sh
# Install Dependencies
COPY scraper_requirements.txt .
RUN pip install -r scraper_requirements.txt

# Delete psycopg2 installed by SQLAlchemy
RUN pip uninstall -y psycopg2

#Install binary version
RUN pip install psycopg2-binary

# Copy the scraper application code and models
COPY lambda_library_scraper.py .
COPY lambda_models.py .
# Command to run the Lambda function
CMD [ "lambda_library_scraper.lambda_handler" ]