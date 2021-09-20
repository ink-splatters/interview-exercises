# syntax=docker/dockerfile:1.2
# Previous line is not a comment
# https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/syntax.md

ARG BASE_IMG=ubuntu
ARG BASE_TAG=21.04

#ARG BASE_IMG=python
#ARG BASE_TAG=3.9.5-slim-buster

FROM ${BASE_IMG}:${BASE_TAG} as base

#ENV PYTHONFAULTHANDLER=1 \
#  PYTHONUNBUFFERED=1 \
#  PYTHONHASHSEED=random \
#  PIP_DEFAULT_TIMEOUT=100 \
#  PIP_CACHE_DIR=/var/cache/pip \
#  GIT_DISCOVERY_ACROSS_FILESYSTEM=1 \
#  PYTHONFAULTHANDLER=1 \
#  PYTHONUNBUFFERED=1 \
#  PYTHONHASHSEED=random \
#  PYTHONDONTWRITEBYTECODE=0 \
#  PURE_GIT_PULL=0

ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ=Europe/Amsterdam

ENV TERM=xterm-color



# making apt cache external using cache mount and prevent it to flush
RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
        echo 'apt::install-recommends "false";' >> /etc/apt/apt.conf && \
        apt update  && apt install -yq vim zsh wget

RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt install -yq libpq-dev apt-utils \
         python3-minimal  python-is-python3 python3-pip # python3.9-venv
