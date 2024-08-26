from django.core.management.base import BaseCommand

from servicos.models import Servico


class Command(BaseCommand):
    def handle(self, *args, **options):
        tipos_servicos_comums_brasil = [
            # Serviços Digitais
            Servico(nome="Desenvolvimento de Sites"),
            Servico(nome="Desenvolvimento de Aplicativos Móveis"),
            Servico(nome="Design Gráfico"),
            Servico(nome="Edição de Vídeo"),
            Servico(nome="Marketing Digital"),
            Servico(nome="Redação de Conteúdo"),
            Servico(nome="Tradução e Localização"),
            Servico(nome="Gerenciamento de Mídias Sociais"),
            Servico(nome="SEO (Otimização para Motores de Busca)"),
            Servico(nome="Desenvolvimento de E-commerce"),
            Servico(nome="Suporte Técnico e Helpdesk"),
            Servico(nome="Consultoria de TI"),
            Servico(nome="Análise de Dados"),
            Servico(nome="Produção de Áudio"),
            Servico(nome="Criação de Apresentações"),
            Servico(nome="Criação de Logotipos"),
            Servico(nome="Design de Interface de Usuário (UI/UX)"),
            Servico(nome="Modelagem 3D e Animação"),
            Servico(nome="Gestão de Projetos"),
            Servico(nome="Consultoria Jurídica"),
            # Serviços Braçais
            Servico(nome="Eletricista"),
            Servico(nome="Encanador"),
            Servico(nome="Pedreiro"),
            Servico(nome="Pintor"),
            Servico(nome="Jardinagem"),
            Servico(nome="Marceneiro"),
            Servico(nome="Montador de Móveis"),
            Servico(nome="Reparos Domésticos"),
            Servico(nome="Instalação de Ar-Condicionado"),
            Servico(nome="Serralheiro"),
            Servico(nome="Manutenção de Eletrodomésticos"),
            Servico(nome="Limpeza Pós-Obra"),
            Servico(nome="Soldador"),
            Servico(nome="Instalação de Pisos e Azulejos"),
            Servico(nome="Carpinteiro"),
            Servico(nome="Gesseiro"),
            Servico(nome="Instalação de Sistemas de Segurança"),
        ]

        Servico.objects.bulk_create(tipos_servicos_comums_brasil)

        self.stdout.write(self.style.SUCCESS("Serviços criados."))
