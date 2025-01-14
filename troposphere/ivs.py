# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 25.0.0


from troposphere import Tags

from . import AWSObject
from .validators import boolean


class Channel(AWSObject):
    resource_type = "AWS::IVS::Channel"

    props = {
        "Authorized": (boolean, False),
        "LatencyMode": (str, False),
        "Name": (str, False),
        "Tags": (Tags, False),
        "Type": (str, False),
    }


class PlaybackKeyPair(AWSObject):
    resource_type = "AWS::IVS::PlaybackKeyPair"

    props = {
        "Name": (str, False),
        "PublicKeyMaterial": (str, True),
        "Tags": (Tags, False),
    }


class StreamKey(AWSObject):
    resource_type = "AWS::IVS::StreamKey"

    props = {
        "ChannelArn": (str, True),
        "Tags": (Tags, False),
    }
