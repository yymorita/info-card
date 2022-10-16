# Games Info

```typescript
class Games{
    title: 'Games Info',
    slug: 'games_info',
    relatedLinks: {
        IGDB_API: 'https://api-docs.igdb.com/#about'
    }
    createdAt: 2022-10-15
    description: 'fetch game information.'
}
```

## 概要

ゲームや書籍などの情報をmarkdown headerとしてアウトプットするモジュール

## テンプレート

```markdown
---
Title: str
RelatedLinks: dict[str, str]
CreatedAt: str
Description: str
---
```

createdAt: 2022-10-16
