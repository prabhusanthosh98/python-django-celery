FROM python:3.5

USER root
# RUN apt-get update && apt-get install -y \
#     htop \
#     vim \
#     less
WORKDIR /root

ADD ./ /root

RUN /root/_install_requirements.sh

CMD ["/root/app.sh"]