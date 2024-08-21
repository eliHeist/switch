from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='style_form')
def style_form(form):
    output = ""

    # Add non-field errors
    if form.non_field_errors():
        output += f"""
        <div class="error_message">
            <ul class="errorlist">
                {''.join(f'<li>{error}</li>' for error in form.non_field_errors())}
            </ul>
        </div>
        """

    # Add fields
    for field in form:
        output += f"""
        <div class="form-control">
            <label class="label" for="{field.id_for_label}">{field.label}</label>
            <div class="field">{field}</div>
            <div class="error_message">{field.errors}</div>
        </div>
        """
    full_output = f'<div class="form-group">{output}</div>'
    return mark_safe(full_output)
