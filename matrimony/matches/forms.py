from django import forms

# creating a form
from .models import BiodataModel
LOCATION = [
        ("Rajasthan" , "Rajasthan"),
        ("Madhya Pradesh" , "Madhya Pradesh"),
        ("Maharashtra" , "Maharashtra"),
        ("Uttar Pradesh" , "Uttar Pradesh"),
        ("Gujarat" , "Gujarat"),
        ("Karnataka" , "Karnataka"),
        ("Andhra Pradesh" , "Andhra Pradesh"),
        ("Odisha" , "Odisha"),
        ("Chhattisgarh" , "Chhattisgarh"),
        ("Tamil Nadu" , "Tamil Nadu"),
        ("Telangana" , "Telangana"),
        ("Bihar" , "Bihar"),
        ("West Bengal" , "West Bengal"),
        ("Arunachal Pradesh" , "Arunachal Pradesh"),
        ("Jharkhand" , "Jharkhand"),
        ("Assam" , "Assam"),
        ("Ladakh" , "Ladakh"),
        ("Himachal Pradesh" , "Himachal Pradesh"),
        ("Uttarakhand" , "Uttarakhand"),
        ("Punjab" , "Punjab"),
        ("Haryana" , "Haryana"),
        ("Jammu and Kashmir" , "Jammu and Kashmir"),
        ("Kerala" , "Kerala"),
        ("Meghalaya" , "Meghalaya"),
        ("Manipur" , "Manipur"),
        ("Mizoram" , "Mizoram"),
        ("Nagaland" , "Nagaland"),
        ("Tripura" , "Tripura"),
        ("Andaman and Nicobar Islands" , "Andaman and Nicobar Islands"),
        ("Sikkim" , "Sikkim"),
        ("Goa" , "Goa"),
        ("Delhi" , "Delhi"),
        ("Dadra and Nagar Haveli and Daman and Diu" , "Dadra and Nagar Haveli and Daman and Diu"),
        ("Puducherry" , "Puducherry"),
        ("Chandigarh" , "Chandigarh"),
        ("Lakshadweep" , "Lakshadweep")
]
Height = [
                ("4 ft 05 in", "4 ft 05 in"),           
                ("4 ft 06 in", "4 ft 06 in"),            
                ("4 ft 07 in", "4 ft 07 in"),            
                ("4 ft 08 in", "4 ft 08 in"),            
                ("4 ft 09 in", "4 ft 09 in"),            
                ("5 ft 09 in", "5 ft 09 in"),            
                ("5 ft 10 in", "5 ft 10 in"),            
                ("5 ft 11 in", "5 ft 11 in"),            
                ("6 ft 00 in", "6 ft 00 in"),             
                ("6 ft 01 in", "6 ft 01 in"),           
                ("6 ft 02 in", "6 ft 02 in"),           
                ("6 ft 03 in", "6 ft 03 in"),            
                ("6 ft 04 in", "6 ft 04 in"),            
                ("6 ft 05 in", "6 ft 05 in"),            
                ("6 ft 06 in", "6 ft 06 in"),             
                ("6 ft 07 in", "6 ft 07 in"),             
                ("6 ft 08 in", "6 ft 08 in"),            
                ("6 ft 09 in", "6 ft 09 in"),             
                ("6 ft 10 in", "6 ft 10 in"),            
                ("6 ft 11 in", "6 ft 11 in"),             
                ("7 ft 00 in", "7 ft 00 in"),             
                ("7 ft 01 in", "7 ft 01 in"),             
                ("7 ft 02 in", "7 ft 02 in"),             
                ("7 ft 03 in", "7 ft 03 in"),             
                ("7 ft 04 in", "7 ft 04 in"),             
                ("7 ft 05 in", "7 ft 05 in"),             
                ("7 ft 06 in", "7 ft 06 in")
]
Nakshatra = [
                ("Select your Nakshatra", "Select your Nakshatra"),
                ("Ashvini/Aswini", "Ashvini/Aswini"),
                ("Bharani", "Bharani"),
                ("Krittika/Krithika", "Krittika/Krithika"),
                ("Rohini", "Rohini"),
                ("Mrigashirsha", "Mrigashirsha"),
                ("Ardra", "Ardra"),
                ("Punarvasu", "Punarvasu"),
                ("Pushya", "Pushya"),
                ("Ashlesha", "Ashlesha"),
                ("Magha", "Magha"),
                ("Purva Phalguni", "Purva Phalguni"),
                ("Uttara Phalguni", "Uttara Phalguni"),
                ("Hasta", "Hasta"),
                ("Chitra", "Chitra"),
                ("Swati", "Swati"),
                ("Vishakha", "Vishakha"),
                ("Anuradha", "Anuradha"),
                ("Jyeshtha", "Jyeshtha"),
                ("Mula", "Mula"),
                ("Purva Ashadha", "Purva Ashadha"),
                ("Uttara Ashadha", "Uttara Ashadha"),
                ("Shravana", "Shravana"),
                ("Dhanishtha", "Dhanishtha"),
                ("Shatabhisha", "Shatabhisha"),
                ("Purva Bhadrapada", "Purva Bhadrapada"),
                ("Uttara Bhadrapada", "Uttara Bhadrapada"),
                ("Revati", "Revati"),
]
Rashi = [
                ("Select your Rashi", "Select your Rashi"),
                ("Aries (Mesh)", "Aries (Mesh)"),
                ("Taurus (Vrushabh)", "Taurus (Vrushabh)"),
                ("Gemini (Mithun)", "Gemini (Mithun)"),
                ("Cancer (Kark)", "Cancer (Kark)"),
                ("Leo (Sinh)", "Leo (Sinh)"),
                ("Virgo (Kanya)", "Virgo (Kanya)"),
                ("Libra (Tula)", "Libra (Tula)"),
                ("Scorpio (Vrushak)", "Scorpio (Vrushak)"),
                ("Sagittarius (Dhanu)", "Sagittarius (Dhanu)"),
                ("Capricorn (Makar)", "Capricorn (Makar)"),
                ("Aquarius (Kumbh)", "Aquarius (Kumbh)"),
                ("Pisces (Meen)", "Pisces (Meen)"),
]
Religion = [
                ("Select your Religion", "Select your Religion"),
                ("Buddhist", "Buddhist"),
                ("Christian", "Christian"),
                ("Hindu", "Hindu"),
                ("Jewish", "Jewish"),
                ("Jain", "Jain"),
                ("Muslim", "Muslim"),
                ("Parsi", "Parsi"),
                ("Silkh", "Sikh"),
                ("Others", "Others"),
]
Manglik = [
            ("Are you Manglik", "Are you Manglik"),
            ("Yes", "Yes"),
            ("No", "No"),
            ("Partial (Anshik)", "Partial (Anshik)"),
]
Education = [
            ("Graduate / Post Graduate / CA / Doctrate", "Graduate / Post Graduate / CA / Doctrate"),("Engineer / B-Tech / M-Tech / BE / ME", "Engineer / B-Tech / M-Tech / BE / ME"),
            ("Doctor / MBBS / BAMS / BHMS MD", "Doctor / MBBS / BAMS / BHMS MD"),
            ("Lawyer / LLB / LLM", "Lawyer / LLB / LLM"),
            ("Diploma / ITI", "Diploma / ITI"),
            ("Pharmacy / B-Pharmacy / M-Pharmacy / D-Pharmacy", "Pharmacy / B-Pharmacy / M-Pharmacy / D-Pharmacy"),
            ("Management / BBA / MBA / Hotel Management", "Management / BBA / MBA / Hotel Management"),
            ("Others", "Others"),
]
Employee = [
            ("Employed in", "Employed in"),
            ("Private Sector", "Private Sector"),
            ("Govt. / Public Sector", "Govt. / Public Sector"),
            ("Civil Services", "Civil Services"),
            ("Defence", "Armed Forces / Defence"),
            ("Business / Self Employed", "Business / Entrepreneur / Self Employed"),
            ("Not Working", "Not Working"),
            ("Others", "Others"),

]
Income = [
            ("Annual Income (in ₹)", "Annual Income (in ₹)"),
            ("No income", "No income"),
            ("0 - 2 Lakhs", "0 - 2 Lakhs"),
            ("2 - 5 Lakhs", "2 - 5 Lakhs"),
            ("5 - 7.5 Lakhs", "5 - 7.5 Lakhs"),
            ("7.5 - 10 Lakhs", "7.5 - 10 Lakhs"),
            ("10 - 15 Lakhs", "10 - 15 Lakhs"),
            ("15 - 20 Lakhs", "15 - 20 Lakhs"),
            ("20 - 25 Lakhs", "20 - 25 Lakhs"),
            ("25 - 50 Lakhs", "25 - 50 Lakhs"),
            ("50 - 75 Lakhs", "50 - 75 Lakhs"),
            ("75 Lakhs - 1 Crore", "75 Lakhs - 1 Crore"),
            ("1 Crore &amp; above", "1 Crore &amp; above"),
]
BrothersSisters = [
            ("Select", "Select"),
            ("0", "0"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
]

class BiodataForm(forms.ModelForm):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    contact = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control'}),required=False)
    place_of_birth = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    sub_place = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    dob = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    timeofBirth = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    caste = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    sub_caste = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    gotra = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    manglik = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=Manglik),required=False)
    rashi = forms.ChoiceField(choices=Rashi,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    nakshatra = forms.ChoiceField(choices=Nakshatra,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    height = forms.ChoiceField(choices=Height,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    religion = forms.ChoiceField(choices=Religion, widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    education = forms.ChoiceField(choices=Education, widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    employee = forms.ChoiceField(choices=Employee, widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    income = forms.ChoiceField(choices=Income,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    college_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    org_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    fname =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    foccupation =forms.ChoiceField(choices=Employee,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    moccupation = forms.ChoiceField(choices=Employee,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    brothers = forms.ChoiceField(choices=BrothersSisters,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    sisters = forms.ChoiceField(choices=BrothersSisters,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    mbrothers = forms.ChoiceField(choices=BrothersSisters,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    msisters = forms.ChoiceField(choices=BrothersSisters,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    address= forms.CharField(max_length=10000,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    mname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    def clean(self):
        cleaned_data = super(BiodataForm, self).clean()
        self.instance.field = 'value'
        return cleaned_data

    class Meta:
        model = BiodataModel
        fields = ['name', 'contact', 'email', 'place_of_birth', 'sub_place', 'dob', 'timeofBirth', 'caste', 'sub_caste', 'gotra', 'manglik', 'rashi', 'nakshatra', 'height', 'religion', 'education', 'employee', 'income', 'college_name', 'org_name', 'fname', 'mname', 'foccupation', 'moccupation', 'brothers', 'sisters', 'mbrothers', 'msisters', 'address']