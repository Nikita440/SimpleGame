from ..models import UserInfo


class ManageUser():
    def changeName(self,nametochange,user):
        table = UserInfo.objects.get(user=user)
        table.name = nametochange
        table.save()