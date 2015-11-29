from django import forms


class NewSubmissionForm(forms.Form):

    PDF = 'PDF'
    WORD = 'WORD'

    paper_format_choice = (
        (PDF, 'PDF'),
        (WORD, 'WORD'),
    )

    topic = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'style': 'width:100%',
                                                                          'class': 'form-control'}))
    author_list = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'style': 'width:100%',
                                                                                'class': 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'style': 'width:100%'}))
    paper_format = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style': 'list-style-type:none'}),
                                     choices=paper_format_choice)
    paper = forms.FileField(label='Upload your paper')
