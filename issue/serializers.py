from rest_framework import serializers
from .models import User, Project, Issue

class SignupSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={"input_type":'password'}, write_only=True) 

    class Meta:
        model = User
        fields = ['email','username','password', 'password_confirm', 'id']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def save(self):
        user = User(email=self.validated_data['email'],
            username =self.validated_data['username'],
            )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']
        if password != password_confirm:
            raise serializers.ValidationError({'password':['Passwords must match']})
        user.set_password(password)
        user.save()
        return user


class ProjectSerializer(serializers.ModelSerializer):
    #assigned_user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many=True)
    #date_posted = serializers.DateTimeField(format='%Y-%m-%d %I:%m %p')
    class Meta:
        model = Project
        fields = ['id','title','description','assigned_user', 'submitted_user', 'date_posted']


class UserSerializer(serializers.ModelSerializer):
    #user_todo_project = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id','priority','status','category','date_posted','date_updated','title','description','assigned_user','submitted_user','project']

