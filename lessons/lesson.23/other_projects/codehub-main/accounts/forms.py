from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import (PasswordChangeForm, UserChangeForm,
                                       UserCreationForm)
from django.forms import HiddenInput
from django.utils.translation import gettext as _

from .models import User


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'crispy-form-item'
            visible.field.widget.attrs['spellcheck'] = 'false'

    class Meta:
        model = User
        fields = ('username', 'email', 'display_name')

    helper = FormHelper()
    helper.add_input(Submit('submit', _('Signup'),
                     css_class='btn-primary crispy-form-item'))


class CustomUserUpdateForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = HiddenInput()

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'crispy-form-item'
            visible.field.widget.attrs['spellcheck'] = 'false'

    class Meta:
        model = User
        fields = ('display_name',
                  'email',
                  'twitter',
                  'github',
                  )

    helper = FormHelper()
    helper.add_input(Submit('submit', _('Update'),
                     css_class='btn-primary crispy-form-item'))


class CustomPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'crispy-form-item'
            visible.field.widget.attrs['spellcheck'] = 'false'

    class Meta:
        model = User

    helper = FormHelper()
    helper.add_input(Submit('submit', _('Update'),
                     css_class='btn-primary crispy-form-item'))
