# -*- coding: utf-8 -*-

# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import logging
import boto3
from botocore.exceptions import ClientError


def retrieve_file(vault_name, archive_ID):
    """Initiate an Amazon Glacier inventory-retrieval job

    To check the status of the job, call Glacier.Client.describe_job()
    To retrieve the output of the job, call Glacier.Client.get_job_output()

    :param vault_name: string
    :return: Dictionary of information related to the initiated job. If error,
    returns None.
    """

    # Construct job parameters
    job_parms = {'Type': 'archive-retrieval'}
    job_parms['ArchiveId'] = archive_ID
                 
    # Initiate the job
    glacier = boto3.client('glacier')
    try:
        response = glacier.initiate_job(vaultName=vault_name,
                                        jobParameters=job_parms)
    except ClientError as e:
        logging.error(e)
        return None
    return response


def main():

    # Assign this value before running the program
    test_vault_name = 'SklarChin'
    archive_ID = '5gedUhLJOVcqNeW5f1SkUbi56C3r1cyewF102GmtRfJztzEsdVBC860qQ0t4BbjRWtu1VB3nUHD1MeRjlHhi9wgqEz9-SKQXyZOyWIZcaqOU0Yb4WG9lLpjU6IprTxf_LExmkeFCqQ'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s')

    # Initiate an inventory retrieval job
    response = retrieve_file(test_vault_name, archive_ID)
    if response is not None:
        logging.info(f'Initiated archive-retrieval job from {test_vault_name}')
        logging.info(f'Retrieval Job ID: {response["jobId"]}')


if __name__ == '__main__':
    main()