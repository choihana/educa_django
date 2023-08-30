from django.forms import inlineformset_factory

from .models import Course, Module

# 외래키로 연결된 1:N 관계의 데이터를 수정 할 때 한번에 여러 데이터를 수정할 수 있게 해준다.
# 필수 입력 인자: 부모모델, 자식모델, 필드명
ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields = ['title','description'],
                                      extra = 2,
                                      can_delete=True
                                      )