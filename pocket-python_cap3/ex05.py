Sub CopiarLinhasSemDuplicacaoDeArquivo()
    ' Caminhos dos arquivos de origem e destino
    Dim caminhoOrigem As String, caminhoDestino As String
    caminhoOrigem = "C:\Caminho\Para\Seu\ArquivoOrigem.xlsx"
    caminhoDestino = "C:\Caminho\Para\Seu\ArquivoDestino.xlsx"
    
    ' Abre os arquivos
    Dim wbOrigem As Workbook, wbDestino As Workbook
    Dim wsOrigem As Worksheet, wsDestino As Worksheet
    Set wbOrigem = Workbooks.Open(caminhoOrigem)
    Set wsOrigem = wbOrigem.Sheets("Planilha1")
    Set wbDestino = Workbooks.Open(caminhoDestino)
    Set wsDestino = wbDestino.Sheets("Planilha1")
    
    Dim ultimaLinhaOrigem As Long, ultimaLinhaDestino As Long
    ultimaLinhaOrigem = wsOrigem.Cells(wsOrigem.Rows.Count, "A").End(xlUp).Row
    ultimaLinhaDestino = wsDestino.Cells(wsDestino.Rows.Count, "A").End(xlUp).Row
    
    ' Loop pelas linhas da origem
    Dim i As Long, j As Long
    Dim linhaIgual As Boolean
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
            wsDestino.Cells(ultimaLinhaDestino, 1).Resize(, 3).Value = wsOrigem.Cells(i, 1).Resize(, 3).Value
        End If
    Next i
    
    ' Salva e fecha os arquivos
    wbDestino.Close SaveChanges:=True
    wbOrigem.Close SaveChanges:=False
    
    MsgBox "Linhas copiadas com sucesso!", vbInformation
End Sub
