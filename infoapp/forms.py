from django.forms import ModelForm

from infoapp.models import Product

from django import forms
from .models import Product, info_list


class ProductCreateForm(forms.ModelForm):
    # 장르들을 체크박스로 정렬하여 선택할 수 있게 한다.
    info_choice = forms.ModelMultipleChoiceField(queryset=info_list.objects.all(),
                                                  widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Product
        #### 참고 : fields 와 exclude 이용법 #####
        # fields = "__all__"
        # fields = ['title','content']
        # exclude = ['title'] #title 필드만 빼고 나머지 필드드로로 Form Field를 생성
        fields = ['title', 'genre_choice', 'developer', 'release_at', 'info', 'pc_requirements_minimum',
                  'pc_requirements_recommended',
                  'thumbnail', 'steam', 'origin', 'uplay', 'epic_games', 'drmfree', 'video']

    def save(self, commit=True):
        # genre 리스트 읽어 하나의 문자열로 변환 뒤 Game(모델)의 genre에 추가
        product = self.instance  # 모델 조회
        info_list = '/'.join([qs.info_list for qs in self.cleaned_data['info_choice']])
        # print(genre_list)
        # Game 모델에 genre 추가
        product.info = info_list
        product.save()  # 모델.salve() => insert
        # print(game.name, game.price, game.genre)
        return product