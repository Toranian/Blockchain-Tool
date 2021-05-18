from django import forms
from .models import Block


class BlockForm(forms.ModelForm):
    
    class Meta:
        model = Block
        fields = ['block_hash']
   
    block_hash = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    ) 
        
    
    def clean_hash(self):
        data = self.cleaned_data.get('block_hash')

        if len(data) < 256:
            raise forms.ValidationError("The hash must be 256 digits in length to be a block hash.")
        return data
    
    def clean(self):
        if 'latest_hash' in self.data:
            return self.data

    # def clean(self):
    #     super(BlockForm, self).clean()
        
    #     block_hash = self.cleaned_date.get('block_hash')

    #     if len(block_hash <= 256):


class TransactionForm(forms.Form):
    
    transaction_hash = forms.CharField(max_length=256)
    
    # def clean(self):
        
    #     super(self).clean()
        
    #     transaction_hash = self.cleaned_data('transaction_hash')
        
    #     if len()
        
        