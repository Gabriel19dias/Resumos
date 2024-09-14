import ttkbootstrap as tb
from ttkbootstrap import Style
import google.generativeai as genai # type: ignore
from tkinter import scrolledtext, messagebox

# Configurar a API
genai.configure(api_key="")

def gerar_resumo():
    texto = texto_entrada.get("1.0", tb.END).strip()
    if not texto:
        messagebox.showwarning("Aviso", "Digite algum texto para resumir.")
        return
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"Resuma o seguinte texto e crie perguntas com respostas depois: {texto}")
        resumo = response.text
        texto_saida.config(state=tb.NORMAL)
        texto_saida.delete("1.0", tb.END)
        texto_saida.insert(tb.END, resumo)
        texto_saida.config(state=tb.DISABLED)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o resumo: {e}")

# Criar a interface gráfica com tema escuro usando ttkbootstrap
def main():
    # Configurar o estilo
    style = Style(theme='darkly')

    # Criar a janela principal
    root = tb.Window()
    root.title("Resumidor de Texto da Brenda")
    
    # Layout
    frame = tb.Frame(root, padding=10)
    frame.pack(expand=True, fill=tb.BOTH)

    # Texto de instruções
    tb.Label(frame, text="Digite o texto para resumir e crie perguntas com respostas depois:", font=("Helvetica", 12)).pack(anchor=tb.W, pady=(0, 10))

    # Área de entrada de texto
    global texto_entrada
    texto_entrada = scrolledtext.ScrolledText(frame, wrap=tb.WORD, height=12, font=("Helvetica", 12))
    texto_entrada.pack(expand=True, fill=tb.BOTH)

    # Botão para gerar resumo
    tb.Button(frame, text="Gerar Resumo", command=gerar_resumo).pack(pady=10)

    # Texto de resumo
    tb.Label(frame, text="Resumo:", font=("Helvetica", 12)).pack(anchor=tb.W, pady=(10, 0))

    # Área de saída de texto
    global texto_saida
    texto_saida = scrolledtext.ScrolledText(frame, wrap=tb.WORD, height=12, font=("Helvetica", 12), state=tb.DISABLED)
    texto_saida.pack(expand=True, fill=tb.BOTH)

    # Iniciar o loop principal da interface gráfica
    root.mainloop()

# Executar a aplicação
if __name__ == "__main__":
    main()
