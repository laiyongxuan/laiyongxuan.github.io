# 赖永炫 · 学术主页

网站地址：https://laiyongxuan.github.io/

GitHub 仓库：https://github.com/laiyongxuan/laiyongxuan.github.io

当前发布源为 `master` 分支的根目录；更新该分支后 GitHub Pages 会自动部署。

中国人民大学信息学院赖永炫的双语学术主页。默认英文首页 `index.html`，中文页面 `zh.html`，顶部可切换语言。公开联系邮箱为 `laiyongxuan@gmail.com`。

适用于 GitHub Pages 的纯静态网站，无付费服务、无追踪脚本。已生成的页面可以直接托管，不需要服务器端运行环境。

## 预览

直接打开 `index.html`，或在本目录运行 `python -m http.server 8000` 后访问 http://localhost:8000 。

## GitHub Pages 免费发布

1. 登录 GitHub，创建公开仓库。个人主页可命名为 `你的用户名.github.io`；也可使用 `academic-homepage` 等项目仓库名。
2. 将 `index.html`、`zh.html`、`style.css`、`.nojekyll` 和 `assets` 文件夹上传至仓库根目录；也可上传本项目全部公开源文件。不要上传原始简历。
3. 打开仓库 **Settings → Pages**，选择 **Deploy from a branch**，分支选实际上传分支（通常为 `main`），目录选 **/(root)**，保存。
4. 等待 Pages 部署成功。个人主页地址为 `https://你的用户名.github.io/`；项目主页为 `https://你的用户名.github.io/仓库名/`。

全部资源使用相对路径，两类地址均兼容。公开仓库可使用 GitHub Free 的 Pages。具体条件见 https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages 。

## 维护内容

- 新论文：编辑 `publications.json`，填写作者、年份、刊物及已核实链接。`published` 表示已发表，`accepted` 表示已录用；`submitted` 会另列为投稿论文。`cv_number` 用于核对原简历 21 条论文，不要在新论文中复用。
- 双语内容：分别编辑 `templates/en.html` 和 `templates/zh.html`。招生内容位于 `id="join"` 区域。未提供当年招生名额，因此不承诺具体名额或录取条件。
- 更新后运行 `python scripts/build_site.py`，重新生成 `index.html` 和 `zh.html`，连同源文件一起提交。生成器仅使用 Python 标准库。
- 项目：所列为简历计划周期，不推断目前是否结题。
- 照片：`assets/portrait.jpg` 从用户提供简历中提取。
- 核验记录见 `SOURCES.md`。已包含简历逐条列出的全部 21 篇论文及 4 篇补充成果（共 25 条，含 1 篇已录用论文），并非全部历史发表目录。

仅保留学术联系邮箱；未包含电话号码、出生日期、政治面貌、项目经费或原始简历文件。
