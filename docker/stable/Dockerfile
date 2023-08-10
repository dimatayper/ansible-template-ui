# Use alpine image as base
FROM alpine
LABEL maintainer="Matt Martz <matt@sivel.net>"

# Copy necessary files
COPY clean_collections.py /tmp/
COPY execute.sh playbook.yml /

# Define dependencies and build dependencies
ENV BUILD_DEPS="py3-pip openssl-dev python3-dev libffi-dev gcc make musl-dev git yaml-dev rust cargo"
ENV RUNTIME_DEPS="python3 openssl ca-certificates"
ENV PIP_PACKAGES="ansible jmespath netaddr"

# Install dependencies, set up environment and clean up
RUN set -x && \
    apk add --no-cache ${RUNTIME_DEPS} ${BUILD_DEPS} && \
    pip3 install -U pip && \
    pip3 install ${PIP_PACKAGES} && \
    python3 /tmp/clean_collections.py && \
    apk del ${BUILD_DEPS} && \
    rm -rf /root/.cache /root/.cargo

CMD ["/bin/sh", "/execute.sh"]
