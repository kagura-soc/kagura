from piccolo.table import Table
from piccolo.columns import Text, UUID, Boolean, ForeignKey, Array, Integer

class KS3Settings(Table):
    id = UUID()
    use_s3 = Boolean(default=False)
    
    base_url = Text()
    bucket = Text()
    prefix = Text()
    endpoint = Text()
    region = Text(default="us-east-1")
    access_key = Text()
    secret_key = Text()
    
    use_ssl = Boolean()
    use_proxy = Boolean()
    public_read_on_upload = Boolean()
    s3_force_path_style = Boolean()

class KMailSettings(Table):
    id = UUID()
    enable_email = Boolean()
    address = Text()
    host = Text()
    port = Integer(default=465)
    username = Text()
    password = Text()
    
    use_ssl = Boolean(default=True)

class KModerationSettings(Table):
    id = UUID()
    
    rules = Array(base_column=Text())
    
    open_registrations = Boolean(default=False)
    
    mail_required = Boolean(default=False)
    disallow_email_domains = Array(base_column=Text())
    
    reserved_names = Array(base_column=Text())
    
    muted_tags = Array(base_column=Text())
    muted_servers = Array(base_column=Text())
    blocked_servers = Array(base_column=Text())
    
    use_mcaptcha = Boolean()
    mcaptcha_instance = Text()
    mcaptcha_site_key = Text()
    mcaptcha_secret_key = Text()
    
    use_turnstile = Boolean()
    turnstile_site_key = Text()
    turnstile_secret_key = Text()
    
    use_hcaptcha = Boolean()
    hcaptcha_site_key = Text()
    hcaptcha_secret_key = Text()
    
    use_recaptcha = Boolean()
    recaptcha_site_key = Text()
    recaptcha_secret_key = Text()
    
    logging_ip = Boolean()

class KSettings(Table):
    id = UUID()
    
    name = Text()
    description = Text()
    
    icon_url = Text()
    icon_192_url = Text()
    icon_512_url = Text()
    
    repository_url = Text(default="https://github.com/kagura-soc/kagura")
    issue_url = Text(default="https://github.com/kagura-soc/kagura/issues")
    
    s3 = ForeignKey(references=KS3Settings)
    moderation = ForeignKey(references=KModerationSettings)
    smtp = ForeignKey(references=KMailSettings)