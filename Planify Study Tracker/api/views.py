from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
import api

from base.models import *
from .serializers import *

# Get API calls
@api_view(['GET'])
def getTables(request):
    tables = Table.objects.all().filter(user=request.user)
    tableSerializer = TableSerializer(tables, many=True)
    return Response(tableSerializer.data)

@api_view(['GET'])
def getTable(request, pk):
    table = Table.objects.all().filter(id=pk)
    tabSerializer = TableSerializer(table, many=True)
    return Response(tabSerializer.data)

@api_view(['GET'])
def getSubjects(request, pk):
    table = Table.objects.all().filter(id=pk)
    subjects = table[0].subjectToTable.all()
    subjectsSerializer = SubjectSerializer(subjects, many=True)
    return Response(subjectsSerializer.data)

@api_view(['GET'])
def getWeeks(request, pk):
    table = Table.objects.all().filter(id=pk)
    weeks = table[0].weekToTable.all()
    weeksSerializer = WeekSerializer(weeks, many=True)
    return Response(weeksSerializer.data)

@api_view(['GET'])
def getNodes(request, pk):
    table = Table.objects.all().filter(id=pk)
    subjects = table[0].subjectToTable.all()
    nodes = []
    for subject in subjects:
        if subject != None:
            nodes.append(subject.nodeSubject.filter(subject=subject))
    n = []
    for i in range(0, len(nodes)):
        for j in range(0, len(nodes[i])):
            try:
                n.append(nodes[i][j])
            except IndexError:
                continue
    nodeSerializer = NodeSerializer(n, many=True)
    return Response(nodeSerializer.data)


# Create API calls
@api_view(['POST'])
def createTable(request):
    serializer = TableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    tableData = {
        "id":serializer.data['id']
    }
    return JsonResponse(tableData)

@api_view(['POST'])
def createSubject(request, pk):
    table = Table.objects.all().filter(id=pk)
    subject = SubjectSerializer(data=request.data)
    if subject.is_valid():
        subject.save()
    weeks = table[0].weekToTable.all()
    for week in weeks:
        data = {
            "user": request.user.id,
            "subject": subject.data['id'],
            "week": week.id
        }
        node = NodeSerializer(data=data)
        if node.is_valid():
            node.save()
    return Response(None)

@api_view(['POST'])
def createWeek(request, pk):
    table = Table.objects.all().filter(id=pk)
    week = WeekSerializer(data=request.data)
    if week.is_valid():
        week.save()
    subjects = table[0].subjectToTable.all()
    for subject in subjects:
        data = {
            "user": request.user.id,
            "subject": subject.id,
            "week": week.data['id']
        }
        node = NodeSerializer(data=data)
        if node.is_valid():
            node.save()
    return Response(None)


# Update API calls
@api_view(['POST'])
def updateTable(request, pk):
    table = Table.objects.get(id=pk)
    serializer = TableSerializer(instance=table, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateSubject(request, pk):
    subject = Subject.objects.get(id=pk)
    subjectData = {
            "name": request.data['name'],
            "table":subject.table.id
        }
    serializer = SubjectSerializer(instance=subject, data=subjectData)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateNode(request, pk):
    node = Node.objects.get(id=pk)
    serializer = NodeSerializer(instance=node, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Delete API calls
@api_view(['POST'])
def deleteTable(request, pk):
    table = Table.objects.all().filter(id=pk)
    table.delete()
    return Response(None)

@api_view(['POST'])
def deleteSubject(request, pk):
    subject = Subject.objects.all().filter(id=pk)
    subject.delete()
    return Response(None)

@api_view(['POST'])
def deleteWeek(request, pk):
    week = Week.objects.all().filter(id=pk)
    week.delete()
    return Response(None)