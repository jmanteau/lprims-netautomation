# pull base image
FROM alpine:3.9


RUN apk --no-cache add \
        sudo \
        openssl \
        ca-certificates \
        sshpass \
        openssh-client \
        rsync
 
RUN apk add --no-cache python3 && \
        python3 -m ensurepip && \
        rm -r /usr/lib/python*/ensurepip && \
        pip3 install --upgrade pip setuptools && \
        if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
        if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 

RUN apk --no-cache add --virtual build-dependencies \
        python3-dev \
        libffi-dev \
        openssl-dev \
        build-base 
    
RUN pip3 install ansible  netaddr pywinrm 

#RUN pip3 install mitogen
    
RUN apk del build-dependencies python3-dev libffi-dev openssl-dev build-base && \
    rm -rf /var/cache/apk/* && \
    rm -r /root/.cache

RUN mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

CMD [ "ansible-playbook", "--version" ]
