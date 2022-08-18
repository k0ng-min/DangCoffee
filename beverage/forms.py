from django import forms
from .models import Product, category_list


class ProductCreateForm(forms.ModelForm):
    # 카테고리들을 체크박스로 정렬하여 선택할 수 있게 한다.
    category_choice = forms.ModelMultipleChoiceField(queryset=category_list.objects.all(),
                                                  widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Product
        # fields = "__all__"
        # fields = ['title','content']
        # exclude = ['title'] #title 필드만 빼고 나머지 필드드로로 Form Field를 생성
        fields = ['korean_name', 'english_name', 'category_choice','description','allergy','kcal','sodium_mg','saturated_fat_g',
                  'sugars_g','protein_g','caffeine_mg','size']

    def product(self, commit=True):
        # category 리스트 읽어 하나의 문자열로 변환 뒤 product의 category에 추가
        product = self.instance  # 모델 조회
        category_list = '/'.join([qs.genre_list for qs in self.cleaned_data['category_choice']])
        # print(category_list)
        # product 모델에 category 추가
        product.category = category_list
        product.save()
        return product