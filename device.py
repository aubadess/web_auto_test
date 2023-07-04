from project.base_api import BaseApi

class Device(BaseApi):

    def add(self,name,label,description):
        url = 'https://thingsboard.stu.hogwarts.ceshiren.com/api/device'
        req = {
            "method":"POST",
            "url":url,
            'json':{
                "name":name,
                "label":label,
                "additonalInfo":{
                    "description":description
                },
            }
        }
        r = self.send_api(req)
        return r

    def search(self):
        url = 'https://thingsboard.stu.hogwarts.ceshiren.com/api/tenant/deviceInfos?pageSize=1000&page=0&sortProperty=createdTime&sortOrder=DESC&deviceProfileId='
        req = {
            "method":"GET",
            "url":url,
        }
        resp = self.send_api(req)
        return resp


    def search_device_id(self, name):
        r = self.search()
        devices = r.json().get('data')
        d = dict()

        for device in devices:
            d[device.get('name')] = device.get('id').get('id')
        return d.get(name)



    def delete(self, name):
        id = self.search_device_id(name)
        url = 'https://thingsboard.stu.hogwarts.ceshiren.com/api/device/' + id
        req = {
            "method": "DELETE",
            "url": url,
            'json': {
                "name": name,
            },
        }
        r = self.send_api(req)
        return r

    def retrive(self, name):
        url = 'https://thingsboard.stu.hogwarts.ceshiren.com/api/tenant/deviceInfos?pageSize=100&page=0'
        req = {
            "method": "get",
            "url": url,
            'params': {
                'textSearch': name
            }
        }
        r = self.send_api(req)
        return r

    def update(self, name, rename, retype):
        id = self.search_device_id(name)
        url = 'https://thingsboard.stu.hogwarts.ceshiren.com/api/device'
        req = {
            "method": "post",
            "url": url,
            'json': {
                "id": {
                    "entityType": "DEVICE",
                    "id": id
                },
                "name": rename,
                "type": retype,
            }
        }
        r = self.send_api(req)
        return r

    def print_info(self, response):
        device_info = response.json().get('data')[0]
        label= device_info.get('label')
        id = device_info.get('id').get('id')
        name = device_info.get('name')
        return [id, name, label]


