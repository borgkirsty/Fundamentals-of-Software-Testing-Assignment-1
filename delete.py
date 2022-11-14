import requests

x = requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')

print(x.status_code)