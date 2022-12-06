# Projeto E-commerce 
Um projeto extremamente simples de e-commerce (ainda incompleto) feito com 
Django 4.0.2 e Python 3.10.2.



### Este projeto NÃO inclui
Abaixo uma lista de recursos que não adicionei ainda e que você pode me ajudar a adicionar.

- Combinações de variações de produto (tem apenas uma variação)
- Cupons de desconto no carrinho de compras
- Cálculo de frete
- Métodos de pagamento (Visa, MasterCard, PayPal, etc...)




### Tutorial
Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:



- Para **Windows**:

```
cd django-simple-ecommerce
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel --user
python -m pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Linux**:

```
cd django-simple-ecommerce
python3.10 -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Mac**

```
cd django-simple-ecommerce
python -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```
FEITO!

