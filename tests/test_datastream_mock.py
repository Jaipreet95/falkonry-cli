# import argparse
# import unittest
# from unittest.mock import Mock, patch, create_autospec
# from .context import falkonry as FalkonryCli
# from falkonryclient import client as Falkonry
# from falkonryclient import schemas as Schemas
# import xmlrunner
#
# class TestDatastream(unittest.TestCase):
#     """Class containing all the tests pertaining to Datastreams"""
#     def setUp(self):
#         self.host = 'https://localhost:8080'
#         self.token = 't6vl8dty74ngy9r4vy29r6pkth4b4npj'
#
#     @patch('falkonry.check_login', return_value=True)
#     @patch('falkonry._falkonry',)
#     def test_do_datastream_get_list(self, mockClient, mockLoggedIn):
#         mockClient.return_value = Mock(Falkonry(host=self.host, token=self.token, options={"header":"falkonry-cli"}))
#         mockClient.get_datastreams = Mock()
#         mockClient.get_datastreams.return_value = []
#         FalkonryCli.REPL.do_datastream_get_list(FalkonryCli.REPL(),'')
#         mockClient.get_datastreams.assert_called_with()
#
#
#     # @patch('falkonry.check_login', return_value=True)
#     # @patch('falkonry._falkonry',)
#     # def test_do_datastream_get_list_with_datastreams(self, mockClient, mockLoggedIn):
#     #     mockClient.side_effect = Mock(Falkonry(host=self.host, token=self.token, options={"header":"falkonry-cli"}))
#     #     mockClient.return_value = Mock(Falkonry(host=self.host, token=self.token, options={"header":"falkonry-cli"}))
#     #     mockClient.get_datastreams = Mock()
#     #
#     #     # mockClient.get_datastreams.return_value = [
#     #     #     {'type': 'entities.Datastream', 'dataSource': {'type': 'STANDALONE'}, 'live': 'ON', 'createdBy': 'qymdt8l48yklrp', 'inputList': [], 'updateTime': 1521117664695,  'name': 'Live1',  'id': 'n8gpyrhpbwwry9', 'timePrecision': 'micro', 'streaming': True,},
#     #     #     {'type': 'entities.Datastream', 'dataSource': {'type': 'STANDALONE'}, 'live': 'ON', 'createdBy': 'qymdt8l48yklrp', 'inputList': [], 'updateTime': 1521117664695,  'name': 'Live1',  'id': 'n8gpyrhpbwwry9', 'timePrecision': 'micro', 'streaming': True,}
#     #     # ]
#     #
#     #     mockClient.get_datastreams.return_value = Mock(Falkonry(host=self.host, token=self.token, options={"header":"falkonry-cli"}).get_datastreams)
#     #     FalkonryCli.REPL.do_datastream_get_list(FalkonryCli.REPL(),'')
#     #     mockClient.get_datastreams.assert_called_with()
#     @patch('argparse.ArgumentParser.parse_args')
#     @patch('falkonry.check_login', return_value=True)
#     @patch('falkonry._falkonry',)
#     def test_do_datastream_get_by_id(self, mockClient, mockLoggedIn,mockedParser):
#         mockClient.return_value = Mock(Falkonry(host=self.host, token=self.token, options={"header":"falkonry-cli"}))
#         mockClient.get_datastream_by_id = []
#         # mockClient.get_datastream_by_id.return_value = []
#         FalkonryCli.REPL.do_datastream_get_by_id(FalkonryCli.REPL(),{'id':''} )
#         mockClient.do_datastream_get_by_id.assert_called_with('id')
#
#
# if __name__ == '__main__':
#     unittest.main(
#         testRunner=xmlrunner.XMLTestRunner(output='out'),
#         failfast=False, buffer=False, catchbreak=False)