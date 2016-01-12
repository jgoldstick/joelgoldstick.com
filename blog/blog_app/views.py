# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
# from django.core.context_processors import csrf
# above depricated, and gone in 1.10
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
# from django.contrib.auth.decorators import login_required
from forms import ContactForm

# cbv
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog_app.models import Entry, Category


def entries_index(request):
    return render_to_response('blog_app/entry_index.html',
                              {'entry_list': Entry.objects.all().filter(status=1)})


class EntryList(ListView):
    model = Entry

from django.core.urlresolvers import reverse_lazy


class EntryCreate(CreateView):
    model = Entry
    success_url = reverse_lazy('Entry-list')


class EntryUpdate(UpdateView):
    model = Entry
    success_url = reverse_lazy('Entry-list')


class EntryDelete(DeleteView):
    model = Entry
    success_url = reverse_lazy('Entry-list')


def entry_detail(request, year, month, day, slug):
    import datetime
    import time
    date_stamp = time.strptime(year + month + day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    return render_to_response('blog_app/entry_detail.html',
                              {'entry': Entry.objects.get(
                                  pub_date__year=pub_date.year,
                                  pub_date__month=pub_date.month,
                                  pub_date__day=pub_date.day,
                                  slug=slug)})


def category_list(request):
    return render_to_response('blog_app/categories_list.html',
                              {'categories': Category.objects.all()})


def entries_by_category(request, category):
    return render_to_response('blog_app/categories_list.html',
                              {'categories': Category.objects.all().filter(title=category)})


class LatestEntriesFeed(Feed):
    title = "JoelGoldstick.com"
    link = "/blog_app/"
    description = "Updates on changes and additions to joelgoldstick.com."

    def items(self):
        return Entry.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt


import random


def produce_expression():
    """
    return a tuple: expression (str), answer (int)
    """
    num_terms = random.randint(2, 3)
    operands = []
    while num_terms:
        n = random.randint(1, 21)
        operands.append(n)
        num_terms -= 1

    result = sum(operands)
    string_operands = map(str, operands)
    expression = " + ".join(string_operands)
    return expression, result

from django.core.mail import send_mail


def contact(request):

    test_expression, answer = produce_expression()
    request.session['last_answer'] = request.session.get('answer', None)
    request.session['answer'] = answer

    #answer = request.session['answer']
    if request.method == 'POST':  # If the form has been submitted...
        # form = ContactForm(request.POST) # A form bound to the POST data
        # A form bound to the POST data
        form = ContactForm(request.POST, request=request)
        if form.is_valid():  # All validation rules pass
            cd = form.cleaned_data
            recipients = ['joel.goldstick@gmail.com']
            if cd['cc_myself']:
                recipients.append(cd['sender'])

            send_mail(cd['subject'], cd['message'], 'from@example.com',
                      recipients, fail_silently=False)

            # Process the data in form.cleaned_data
            #request.session['answer'] = ""
            # Redirect after POST
            return HttpResponseRedirect(reverse('index'))
            # return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm()  # An unbound form

    c = {'form': form, 'test': test_expression}
    c.update(csrf(request))
    return render_to_response('blog_app/contact_form.html', c)
