from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def home(request):
    return render(request, 'App/home.html')
# Character Views
def char_list(request):
    characters = Character.objects.all()
    return render(request, 'App/char_list.html', {'char_list': characters})

def char_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'App/char_detail.html', {'character': character})

def char_new(request):
    if request.method == "POST":
        form = CharForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.save()
            return redirect('char_detail', pk=character.pk)
    else:
        form = CharForm()
    return render(request, 'App/char_edit.html', {'form': form})

def char_edit(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        form = CharForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.save()
            return redirect('char_detail', pk=character.pk)
    else:
        form = CharForm(instance=character)
    return render(request, 'App/char_edit.html', {'form': form})

def char_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        character.delete()
        return redirect('char_list')
    return render(request, 'App/char_detail.html', {'character': character})

# Spell Views
def spell_list(request):
    spells = Spells.objects.all()
    return render(request, 'App/spell_list.html', {'spell_list': spells})

def spell_detail(request, pk):
    spell = get_object_or_404(Spells, pk=pk)
    return render(request, 'App/spell_detail.html', {'spell': spell})

def spell_new(request):
    if request.method == "POST":
        form = SpellForm(request.POST)
        if form.is_valid():
            spell = form.save(commit=False)
            spell.save()
            return redirect('spell_detail', pk=spell.pk)
    else:
        form = SpellForm()
    return render(request, 'App/spell_edit.html', {'form': form})

def spell_edit(request, pk):
    spell = get_object_or_404(Spells, pk=pk)
    if request.method == "POST":
        form = SpellForm(request.POST, instance=spell)
        if form.is_valid():
            spell = form.save(commit=False)
            spell.save()
            return redirect('spell_detail', pk=spell.pk)
    else:
        form = SpellForm(instance=spell)
    return render(request, 'App/spell_edit.html', {'form': form})

def spell_delete(request, pk):
    spell = get_object_or_404(Spells, pk=pk)
    if request.method == "POST":
        spell.delete()
        return redirect('spell_list')
    return render(request, 'App/spell_detail.html', {'spell': spell})

# Class Views
def class_list(request):
    classes = Classes.objects.all()
    return render(request, 'App/class_list.html', {'class_list': classes})

def class_detail(request, pk):
    class_obj = get_object_or_404(Classes, pk=pk)
    return render(request, 'App/class_detail.html', {'class': class_obj})

def class_new(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            class_obj = form.save(commit=False)
            class_obj.save()
            return redirect('class_detail', pk=class_obj.pk)
    else:
        form = ClassForm()
    return render(request, 'App/class_edit.html', {'form': form})

def class_edit(request, pk):
    class_obj = get_object_or_404(Classes, pk=pk)
    if request.method == "POST":
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            class_obj = form.save(commit=False)
            class_obj.save()
            return redirect('class_detail', pk=class_obj.pk)
    else:
        form = ClassForm(instance=class_obj)
    return render(request, 'App/class_edit.html', {'form': form})

def class_delete(request, pk):
    class_obj = get_object_or_404(Classes, pk=pk)
    if request.method == "POST":
        class_obj.delete()
        return redirect('class_list')
    return render(request, 'App/class_detail.html', {'class': class_obj})

# Trait Views
def trait_list(request):
    traits = Traits.objects.all()
    return render(request, 'App/trait_list.html', {'trait_list': traits})

def trait_detail(request, pk):
    trait = get_object_or_404(Traits, pk=pk)
    return render(request, 'App/trait_detail.html', {'trait': trait})

def trait_new(request):
    if request.method == "POST":
        form = TraitForm(request.POST)
        if form.is_valid():
            trait = form.save(commit=False)
            trait.save()
            return redirect('trait_detail', pk=trait.pk)
    else:
        form = TraitForm()
    return render(request, 'App/trait_edit.html', {'form': form})

def trait_edit(request, pk):
    trait = get_object_or_404(Traits, pk=pk)
    if request.method == "POST":
        form = TraitForm(request.POST, instance=trait)
        if form.is_valid():
            trait = form.save(commit=False)
            trait.save()
            return redirect('trait_detail', pk=trait.pk)
    else:
        form = TraitForm(instance=trait)
    return render(request, 'App/trait_edit.html', {'form': form})

def trait_delete(request, pk):
    trait = get_object_or_404(Traits, pk=pk)
    if request.method == "POST":
        trait.delete()
        return redirect('trait_list')
    return render(request, 'App/trait_detail.html', {'trait': trait})