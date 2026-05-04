import interface.menu as menu
import sistemas.sistema as sistema 

def iniciar():
    
    print("="*60)
    print(f"{'SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS':^60}")
    print(f"{'FACULDADES AEMS - CURSO TADS':^60}")
    print("="*60)

    print("\n[ STATUS ] Banco de dados inicial carregado com sucesso.")

    try:
        menu.exibir_menu()
    except Exception as e:
        print(f"\n[ ERRO ] Ocorreu uma falha no sistema: {e}")
    finally:
        print("\n" + "="*60)
        print(f"{'SISTEMA ENCERRADO':^60}")
        print("="*60)

if __name__ == "__main__":
    iniciar()