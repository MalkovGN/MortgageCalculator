from django.shortcuts import render, redirect

from .forms import MortgageInfoForm
from .models import MortgageInfo


def calc_page(request):
    if request.method == 'GET':
        return render(request, 'mortgage_calc_app/calc_page.html', {'mortgage_form': MortgageInfoForm})
    else:
        # try:
            mortgage_form = MortgageInfoForm(request.POST)
            new_form = mortgage_form.save(commit=False)
            new_form.save()
            return redirect('calc_page')

