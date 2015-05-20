# django
from pprint import pprint
import user
from django.contrib import messages
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#lib
import json
import ast

#local
from functions import *
from models import contacts, contactgroup, device, User, msgTemplates
from .forms import SendMsgForm, AddContactForm, AddContactToGroupForm, createTemplateForm

# Create your views here.



@login_required
def sendSMS(request):
    form = SendMsgForm(request.POST or None)
    if form.is_valid():
        number = form.cleaned_data['phoneNumber']
        number_list = number.split(", ")
        message = form.cleaned_data['message']
        deviceID = request.POST.get('deviceID')
        device_obj = device.objects.all()
        for d_obj in device_obj:
            if d_obj.user == request.user:
                for num in number_list:
                    accountEmail = d_obj.accountEmail
                    accountPassword = d_obj.accountPassword
                    gateway = SmsGateway()
                    gateway.loginDetails(accountEmail, accountPassword)
                    gateway.sendMessageToNumber(num, message, deviceID)
        messages.success(request, 'Message Envoye')
        return redirect('/messages/0')
    username = request.user.username
    device_obj = device.objects.all()
    contact_list = contacts.objects.filter(user=request.user)
    group_list = contactgroup.objects.filter(contact__user=request.user).distinct()
    template_list = msgTemplates.objects.filter(user=request.user).distinct()
    context = {"form": form}
    template = "sendsms.html"
    pg = ['active', '', '']
    return render_to_response(template, locals(), context_instance=RequestContext(request))


@login_required
def getMessages(request, page):
    device_obj = device.objects.filter(user=request.user)
    contact_obj = contacts.objects.filter(user=request.user)
    msgs = []
    for d_obj in device_obj:
        accountEmail = d_obj.accountEmail
        accountPassword = d_obj.accountPassword
        gateway = SmsGateway()
        gateway.loginDetails(accountEmail, accountPassword)
        json_string = gateway.getMessages()
    for msg in json_string['response']['result']:
        msgs.append({
            "status": msg['status'],
            "sent_at": msg['sent_at'],
            "received_at": msg['received_at'],
            "contact_number": msg['contact']['number'],
            "message": msg['message']})
    pagesize = 10
    pages = range(((len(msgs) - 1) / pagesize) + 1)
    active = int(page)
    msgs = msgs[(active * pagesize):(active * pagesize) + pagesize]
    pg = ['', 'active', '']
    return render_to_response('messages.html', locals(), context_instance=RequestContext(request))


@login_required
def viewContact(request, page):
    contact_list = contacts.objects.filter(user=request.user)
    form = AddContactForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.user = request.user
        save_it.save()
        messages.success(request, 'Contact Saved')
        return HttpResponseRedirect('')

    contact_group = contactgroup.objects.filter(user=request.user)
    groupForm = AddContactToGroupForm(request.POST or None)
    if groupForm.is_valid():
        cg = contactgroup()
        cg.user = request.user
        cg.groupName = groupForm.cleaned_data['groupName']
        checklist = request.POST.getlist('checks[]')
        cg.save()
        for num in checklist:
            c = contacts.objects.filter(user=request.user).get(phoneNumber=num)
            cg.contact.add(c)
        return HttpResponseRedirect('')
    active = int(page)
    pagesize = 10
    pages = range(((len(contact_list) - 1) / pagesize) + 1)
    contacts_pag = contact_list[active * pagesize: (active * pagesize) + pagesize]
    pg = ['', '', 'active']
    return render_to_response('contacts.html', locals(), context_instance=RequestContext(request))


@login_required
def editContact(request, num):
    contact = contacts.objects.filter(user=request.user).get(phoneNumber=num)
    form = AddContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.user = request.user
        save_it.save()
        return redirect('/contacts/0')
    return render_to_response('editcontact.html', locals(), context_instance=RequestContext(request))


@login_required
def deleteContact(request, num):
    contact = contacts.objects.filter(user=request.user).get(phoneNumber=num)
    contact.delete()
    return redirect('/contacts/0')


@login_required
def createTemplate(request):
    template = msgTemplates.objects.filter(user=request.user)
    form = createTemplateForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.user = request.user
        save_it.save()
        return redirect('/send-sms/')
    return render_to_response('createtemplate.html', locals(), context_instance=RequestContext(request))

@login_required
def editTemplate(request, templateID):
    template = msgTemplates.objects.filter(user=request.user).get(id=templateID)
    form = createTemplateForm(request.POST or None, instance=template)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.user = request.user
        save_it.save()
        return redirect('/template/')
    return render_to_response('edittemplate.html', locals(), context_instance=RequestContext(request))

@login_required
def deleteTemplate(request, templateID):
    template = msgTemplates.objects.filter(user=request.user).get(id=templateID)
    template.delete()
    return redirect('/template/')

@login_required
def sandbox(request):
    form = SendMsgForm(request.POST or None)
    if form.is_valid():
        number = form.cleaned_data['phoneNumber']
        selected_contacts = request.POST.getlist['contacts']
        number_list = number.split(", ")
        number_list.append(selected_contacts)
        message = form.cleaned_data['message']
        deviceID = request.POST.get('deviceID')
        device_obj = device.objects.all()
        for d_obj in device_obj:
            if d_obj.user == request.user:
                for num in number_list:
                    accountEmail = d_obj.accountEmail
                    accountPassword = d_obj.accountPassword
                    gateway = SmsGateway()
                    gateway.loginDetails(accountEmail, accountPassword)
                    gateway.sendMessageToNumber(num, message, deviceID)
        messages.success(request, 'Message Envoye')
        return redirect('/messages/0')
    username = request.user.username
    device_obj = device.objects.all()
    contact_list = contacts.objects.filter(user=request.user)
    group_list = contactgroup.objects.filter(contact__user=request.user).distinct()
    template_list = msgTemplates.objects.filter(user=request.user).distinct()
    context = {"form": form}
    template = "sendsms2.html"
    pg = ['active', '', '']
    return render_to_response(template, locals(), context_instance=RequestContext(request))