# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double
from .validators.transfer import validate_homedirectory_type


class EndpointDetails(AWSProperty):
    """
    `EndpointDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html>`__
    """

    props: PropsDictType = {
        "AddressAllocationIds": ([str], False),
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
        "VpcEndpointId": (str, False),
        "VpcId": (str, False),
    }


class IdentityProviderDetails(AWSProperty):
    """
    `IdentityProviderDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html>`__
    """

    props: PropsDictType = {
        "DirectoryId": (str, False),
        "Function": (str, False),
        "InvocationRole": (str, False),
        "Url": (str, False),
    }


class ProtocolDetails(AWSProperty):
    """
    `ProtocolDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html>`__
    """

    props: PropsDictType = {
        "PassiveIp": (str, False),
        "TlsSessionResumptionMode": (str, False),
    }


class WorkflowDetail(AWSProperty):
    """
    `WorkflowDetail <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html>`__
    """

    props: PropsDictType = {
        "ExecutionRole": (str, True),
        "WorkflowId": (str, True),
    }


class WorkflowDetails(AWSProperty):
    """
    `WorkflowDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html>`__
    """

    props: PropsDictType = {
        "OnUpload": ([WorkflowDetail], True),
    }


class Server(AWSObject):
    """
    `Server <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html>`__
    """

    resource_type = "AWS::Transfer::Server"

    props: PropsDictType = {
        "Certificate": (str, False),
        "Domain": (str, False),
        "EndpointDetails": (EndpointDetails, False),
        "EndpointType": (str, False),
        "IdentityProviderDetails": (IdentityProviderDetails, False),
        "IdentityProviderType": (str, False),
        "LoggingRole": (str, False),
        "ProtocolDetails": (ProtocolDetails, False),
        "Protocols": ([str], False),
        "SecurityPolicyName": (str, False),
        "Tags": (Tags, False),
        "WorkflowDetails": (WorkflowDetails, False),
    }


class HomeDirectoryMapEntry(AWSProperty):
    """
    `HomeDirectoryMapEntry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html>`__
    """

    props: PropsDictType = {
        "Entry": (str, True),
        "Target": (str, True),
    }


class PosixProfile(AWSProperty):
    """
    `PosixProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html>`__
    """

    props: PropsDictType = {
        "Gid": (double, True),
        "SecondaryGids": ([double], False),
        "Uid": (double, True),
    }


class User(AWSObject):
    """
    `User <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html>`__
    """

    resource_type = "AWS::Transfer::User"

    props: PropsDictType = {
        "HomeDirectory": (str, False),
        "HomeDirectoryMappings": ([HomeDirectoryMapEntry], False),
        "HomeDirectoryType": (validate_homedirectory_type, False),
        "Policy": (str, False),
        "PosixProfile": (PosixProfile, False),
        "Role": (str, True),
        "ServerId": (str, True),
        "SshPublicKeys": ([str], False),
        "Tags": (Tags, False),
        "UserName": (str, True),
    }


class WorkflowStep(AWSProperty):
    """
    `WorkflowStep <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html>`__
    """

    props: PropsDictType = {
        "CopyStepDetails": (dict, False),
        "CustomStepDetails": (dict, False),
        "DeleteStepDetails": (dict, False),
        "TagStepDetails": (dict, False),
        "Type": (str, False),
    }


class Workflow(AWSObject):
    """
    `Workflow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html>`__
    """

    resource_type = "AWS::Transfer::Workflow"

    props: PropsDictType = {
        "Description": (str, False),
        "OnExceptionSteps": ([WorkflowStep], False),
        "Steps": ([WorkflowStep], True),
        "Tags": (Tags, False),
    }
