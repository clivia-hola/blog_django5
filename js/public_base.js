window.onload = function() {
  const { createEditor, createToolbar } = window.wangEditor

  const editorConfig = {
    placeholder: 'Type here...',
    onChange(editor) {
      const html = editor.getHtml()
      console.log('editor content', html)
      // 也可以同步到 <textarea>
    },
  }

  const editor = createEditor({
    selector: '#editor-container',
    html: '<p><br></p>',
    config: editorConfig,
    mode: 'default', // or 'simple'
  })

  const toolbarConfig = {}

  const toolbar = createToolbar({
    editor,
    selector: '#toolbar-container',
    config: toolbarConfig,
    mode: 'default', // or 'simple'
  })

  $("#submit-up").click(function (event) {
  //阻止按钮的默认行为
    event.preventDefault();
    //获取表单数据
    let title = $("input[name='title']").val();
    let category=$("#category-select").val();
    let content = editor.getHtml();
    let csrfmiddlewaretoken=$("input[name='csrfmiddlewaretoken']").val();
    $.ajax("/blog/pub",{
        method: "POST",
        data:{title,category,content,csrfmiddlewaretoken},
        success:function(result) {
          console.log(result);
          if (result.code == 200) {
            //获取博客id
            let blog_id=result['data']['blog_id'];
            window.location = blog_id;
          }else{
            alert(result.message);
          }
      }
    })
  });
}