Sub CopiarLinhasSemDuplicacaoDeArquivo()
    ' Caminhos dos arquivos de origem e destino
    Dim caminhoOrigem As String
    Dim caminhoDestino As String
    caminhoOrigem = "C:\Caminho\Para\Seu\ArquivoOrigem.xlsx"
    caminhoDestino = "C:\Caminho\Para\Seu\ArquivoDestino.xlsx"
    
    ' Declara e abre os arquivos
    Dim wbOrigem As Workbook
    Dim wbDestino As Workbook
    Dim wsOrigem As Worksheet
    Dim wsDestino As Worksheet
    Set wbOrigem = Workbooks.Open(caminhoOrigem)
    Set wsOrigem = wbOrigem.Sheets("Planilha1")
    Set wbDestino = Workbooks.Open(caminhoDestino)
    Set wsDestino = wbDestino.Sheets("Planilha1")
    
    ' Encontra a última linha com dados em cada planilha
    Dim ultimaLinhaOrigem As Long
    Dim ultimaLinhaDestino As Long
    ultimaLinhaOrigem = wsOrigem.Cells(wsOrigem.Rows.Count, "A").End(xlUp).Row
    ultimaLinhaDestino = wsDestino.Cells(wsDestino.Rows.Count, "A").End(xlUp).Row
    
    Dim i As Long
    Dim j As Long
    Dim linhaIgual As Boolean
    
    ' Loop pelas linhas da origem
    For i = 1 To ultimaLinhaOrigem
        linhaIgual = False
        
        ' Verifica se a linha já existe na planilha de destino
        For j = 1 To ultimaLinhaDestino
            If wsOrigem.Cells(i, 1).Value = wsDestino.Cells(j, 1).Value And _
               wsOrigem.Cells(i, 2).Value = wsDestino.Cells(j, 2).Value And _
               wsOrigem.Cells(i, 3).Value = wsDestino.Cells(j, 3).Value Then
                linhaIgual = True
                Exit For
            End If
        Next j
        
        ' Se a linha não for duplicada, copia para a planilha de destino
        If Not linhaIgual Then
            ultimaLinhaDestino = ultimaLinhaDestino + 1
            wsDestino.Cells(ultimaLinhaDestino, 1).Resize(1, 3).Value = wsOrigem.Cells(i, 1).Resize(1, 3).Value
        End If
    Next i
    
    ' Salva e fecha os arquivos
    wbDestino.Close SaveChanges:=True
    wbOrigem.Close SaveChanges:=False
    
    MsgBox "Linhas copiadas com sucesso!", vbInformation
End Sub

