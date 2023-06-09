# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_darabonba_stream.client import Client as StreamClient
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> ocr_api20210707Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def create_client_with_sts(
        access_key_id: str,
        access_key_secret: str,
        security_token: str,
    ) -> ocr_api20210707Client:
        """
        使用STS鉴权方式初始化账号Client，推荐此方式。
        @param access_key_id:
        @param access_key_secret:
        @param security_token:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret,
            # 必填，您的 Security Token,
            security_token=security_token,
            # 必填，表明使用 STS 方式,
            type='sts'
        )
        # 访问的域名
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client('ACCESS_KEY_ID', 'ACCESS_KEY_SECRET')
        # 需要安装额外的依赖库，直接点击下载完整工程即可看到所有依赖。
        body_stream = StreamClient.read_from_file_path('<your-file-path>')
        recognize_advanced_request = ocr_api_20210707_models.RecognizeAdvancedRequest(
            body=body_stream
        )
        runtime = util_models.RuntimeOptions()
        resp = client.recognize_advanced_with_options(recognize_advanced_request, runtime)
        ConsoleClient.log(UtilClient.to_jsonstring(resp))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client('ACCESS_KEY_ID', 'ACCESS_KEY_SECRET')
        # 需要安装额外的依赖库，直接点击下载完整工程即可看到所有依赖。
        body_stream = StreamClient.read_from_file_path('<your-file-path>')
        recognize_advanced_request = ocr_api_20210707_models.RecognizeAdvancedRequest(
            body=body_stream
        )
        runtime = util_models.RuntimeOptions()
        resp = await client.recognize_advanced_with_options_async(recognize_advanced_request, runtime)
        ConsoleClient.log(UtilClient.to_jsonstring(resp))


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
