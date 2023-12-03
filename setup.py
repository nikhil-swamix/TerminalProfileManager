from py2exe import freeze
import pythonnet

print(dir(pythonnet))

# test pythonnet
import clr
clr.AddReference("System.Windows.Forms")
# # Setup
# freeze(
#     console=['main.py'],
#     windows=[],
#     data_files=None,
#     zipfile='library.zip',
#     version_info={},
#     options={
#         "bundle_files": 2,
#         "includes": ['pythonnet', 'webview', 'json', 'os'],
#     },
# )
