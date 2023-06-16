from django.db import models

# Create your models here.

class Order(models.Model):
    # on_delete : 연결된 외래키 아이템이 삭제될 때 해당 Order 아이템을 어떻게 지워줄지
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="사용자")
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="제품")
    quantity = models.IntegerField(verbose_name="수량")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="주문날짜")

    class Meta:
        db_table = 'shoppingmall_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'

