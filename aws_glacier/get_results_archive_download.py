
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

import json
import io
import logging
import boto3
from botocore.exceptions import ClientError


def write_streamingbody_to_file(sb, archive_name):
    import io
    with io.FileIO(archive_name, 'wb') as file:
        while file.write(sb.read(amt=512)):
            pass



def retrieve_archivefetch_results(vault_name, job_id):
    """Retrieve the results of an Amazon Glacier inventory-retrieval job

    :param vault_name: string
    :param job_id: string. The job ID was returned by Glacier.Client.initiate_job()
    :return: Dictionary containing the results of the inventory-retrieval job.
    If error, return None.
    """

    # Retrieve the job results
    glacier = boto3.client('glacier')
    job_results_in_dict = glacier.get_job_output(vaultName=vault_name, jobId=job_id)
    
    sb = job_results_in_dict['body']
    filename = job_results_in_dict['archiveDescription']
    write_streamingbody_to_file(sb, '../frontthin-lm_SensiVault_L0_2018_04_18_55793.taz.gpg')
    
    




def main():

    # Assign these values before running the program
    vault_name = 'SklarChin'
    job_id = '2bArs0bGcjImOr42E1OU1MAaC2JXESAuMRWfO_NjZrLAdOMVtBJPinblt6jZkovSOONa4IqfgopxsgaNnyLcWj6Tp-CU'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve the job results
    inventory = retrieve_archivefetch_results(vault_name, job_id)
    if inventory is not None:
        # Output some of the inventory information
        logging.info(f'Vault ARN: {inventory["VaultARN"]}')
        for archive in inventory['ArchiveList']:
            logging.info(f'  Size: {archive["Size"]:6d}  '
                         f'Archive ID: {archive["ArchiveId"]}')


if __name__ == '__main__':
    main()
