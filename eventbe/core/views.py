from django.shortcuts import render


def custom_page_not_found_view(request, exception=None):
    return render(request, 'errors/404.html', context={})


def custom_error_view(request, exception=None):
    return render(request, 'errors/500.html', context={})


def custom_permission_denied_view(request, exception=None):
    return render(request, 'errors/403.html', context={})


def custom_bad_request_view(request, exception=None):
    return render(request, 'errors/400.html', context={})
