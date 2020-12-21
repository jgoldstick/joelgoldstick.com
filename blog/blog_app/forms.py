from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(required=True)
    sender = forms.EmailField(required=True)
    test_result = forms.IntegerField(label="Test Result", required=True)
    cc_myself = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(ContactForm, self).__init__(*args, **kwargs)

    def clean_test_result(self):
        data = self.cleaned_data["test_result"]
        if self.request.session["last_answer"] != data:
            raise forms.ValidationError("You didn't get the math right!")


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
