import os, glob, json, time, re
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from notasquare.urad_api.containers.standard import Container
from application.models import *
from application.helpers import common as common_helper


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print "XXX"
