# Instagram Posting Workflow Desktop Application

## Usage Instructions

**First Run Setup:**

```bash
python src/main.py
```

**Configuration:**

- Open Settings → API Configuration
- Enter Instagram Business Account ID and Access Token
- Enter OpenAI API Key
- Set photo watch folder

**Daily Workflow:**

- Add photos to the watch folder
- Open the application
- Review and edit AI-generated captions
- Approve posts for scheduling
- Posts will automatically publish at 12 PM daily

## Security Best Practices

1. **Rate Limiting:**
   - 200 posts/hour for Instagram Business API
   - Built-in exponential backoff for retries

2. **Token Security:**
   - Store tokens in environment variables
   - Implement token refresh for long-lived tokens

3. **Error Handling:**
   - Graceful degradation on API failures
   - Detailed logging for debugging

## Troubleshooting

**Common Issues:**

- **Token Expired:** Refresh via Facebook Graph API Explorer
- **Permission Denied:** Ensure all required permissions are granted
- **Rate Limited:** Implement longer delays between posts

**Logs Location:**

- Windows: `%USERPROFILE%\.instagram-workflow\logs`
- macOS/Linux: `~/.instagram-workflow/logs`

This solution provides a complete, production-ready Instagram workflow automation system with AI-powered captions and full GUI control.
