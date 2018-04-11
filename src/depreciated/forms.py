from django import forms


Suppliers = (
	('AMTI','AMTI'),
	('Apple','Apple'),
	('Arkphire','Arkphire'),
	('CDW','CDW'),
	('Dell','Dell'),
	('DYHL','DYHL'),
	('Gadgets','Gadgets'),
	('Gownet','Gownet'),
	('HP','HP'),
	('Lenovo','Lenovo'),
	('Moredirect','Moredirect'),
	('Workplace','Workplace'),
	('Zones','Zones'))

Regions = ('APAC','EMEA','NAMER','MTV','LATAM')

class EoLForm(forms.Form):
	partnumber = forms.CharField()
	productname = forms.CharField()
	
	supplier = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),choices=Suppliers,)
	
	region = forms.MultipleChoiceField()
	country = forms.MultipleChoiceField()
	
	fromdate = forms.DateField(widget=forms.DateInput())
	todate = forms.DateField()