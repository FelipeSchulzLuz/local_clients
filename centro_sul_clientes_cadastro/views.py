from django.shortcuts import render
from .models import Cliente
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .forms import PostForm, PostFormEdit
from django.views.generic.list import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.

class ClienteListView(ListView):   
    model = Cliente
    paginated_by = 10
    template_name = 'cliente_list.html'
    context_object_name = 'Cliente'

    def get_queryset(self):
        queryset = Cliente.objects.all()
        if self.request.GET.get('publish'):
            queryset = queryset.filter(publish__icontains=self.request.GET.get('publish'))

        return queryset.order_by('-status')

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        clientes = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(clientes, '30')
        try:
            clientes = paginator.page(page)
        except PageNotAnInteger:
            clientes = paginator.page(1)
        except EmptyPage:
            clientes = paginator.page(paginator.num_pages)
        context['clientes'] = clientes
        context['nome_cliente'] = self.request.GET.get('nome_cliente', '')
        return context

    


def home(request):
    clientes = Cliente.objects.all().order_by("status")
    return render(request, 'home.html', {'clientes': clientes})



def detalhe_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'detalhe_cliente.html', {'cliente': cliente})

def delete(request, pk):
    transacao = Transacao.Cliente.get(pk=pk)
    transacao.delete()
    return redirect('home')


def adicionar_cliente(request):
    #Quando para salvar
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.autor = request.user         
            cliente.save()
            return redirect('home')
    else:
        form = PostForm() 

    return render(request, 'edit_cliente.html', {'form':form})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = PostFormEdit(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('home')
    else:
        form = PostFormEdit(instance=cliente)

    return render(request, 'edit_cliente.html', {'form':form})


def lista_cliente(request):
    def get_queryset(self):
        return super(lista_cliente,self).get_queryset().filter(status='condicao_atendimento')
    def get_absolute_url(self):
        return reverse('centro_sul_clientes_cadastro:cliente_list', args=[self.publish.year, self.publish.month, self.publish.day, slugify(self.slug)])
    return render(request, 'cliente_list.html')   
