from django.shortcuts import render, redirect
from . models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contacts(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing = request.POST.get('listing')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            is_present = Contact.objects.filter(user_id = user_id, listing_id = listing_id)
            if is_present:
                messages.error(request, "You've already made an inquiry for this listing.")
                return redirect('/listings/' + listing_id)


        contact = Contact(user_id = user_id, listing_id = listing_id, listing = listing, name = name, email = email, phone = phone, message = message )
        contact.save()

        send_mail(
            'Property Listing Inquiry',
            'There has been inquiry for ' + listing + '. Sign in to the admin panel for more details.',
            'simranpanthi52@gmail.com',
            [realtor_email, 'samippanthi@gmail.com']
        )

        messages.success(request, "Your request have been submitted. A realtor will get back to you soon.")
        return redirect('/listings/' + listing_id)