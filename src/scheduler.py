from database import bulk_insert_phishing_url
from phishing import (
    get_phishing_url_from_txt,
    get_alienvault_phishing_feed,
    get_tweet_phishing_feed,
    get_phishtank_feed,
)
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from dynaconf import Dynaconf

settings = Dynaconf(settings_file="settings.toml")


async def main():
    scheduler = AsyncIOScheduler()

    # İlk olarak tüm taskleri bir kere çalıştırmak için, ayrıca tüm tasklerin bitmesini beklemek için bir coroutine tanımlayalım.
    async def run_all_tasks_once() -> None:
        """
        Run tasks once at program startup.

        Args:
            None.

        Returns:
            Returns None.
        """

        await bulk_insert_phishing_url(
            await get_phishing_url_from_txt(settings.feeds.usom_feed)
        )
        await bulk_insert_phishing_url(
            await get_phishing_url_from_txt(settings.feeds.urlhaus_feed)
        )
        await bulk_insert_phishing_url(
            await get_alienvault_phishing_feed(settings.feeds.alienvault_vetted)
        )
        await bulk_insert_phishing_url(
            await get_alienvault_phishing_feed(settings.feeds.alienvault_turkey)
        )
        await bulk_insert_phishing_url(
            await get_alienvault_phishing_feed(settings.feeds.alienvault_domain)
        )
        await bulk_insert_phishing_url(
            await get_alienvault_phishing_feed(settings.feeds.alienvault_url)
        )
        await bulk_insert_phishing_url(
            await get_tweet_phishing_feed(settings.feeds.tweet_feed)
        )
        await get_phishtank_feed(settings.feeds.phishtank_feed)

    await run_all_tasks_once()

    # I added the tasks to run every hour.
    scheduler.add_job(
        bulk_insert_phishing_url,
        "interval",
        hours=1,
        args=(await get_phishing_url_from_txt(settings.feeds.usom_feed),),
    )
    scheduler.add_job(
        bulk_insert_phishing_url,
        "interval",
        hours=1,
        args=(await get_phishing_url_from_txt(settings.feeds.urlhaus_feed),),
    )
    scheduler.add_job(
        bulk_insert_phishing_url,
        "interval",
        hours=1,
        args=(await get_alienvault_phishing_feed(settings.feeds.alienvault_vetted),),
    )
    scheduler.add_job(
        bulk_insert_phishing_url,
        "interval",
        hours=1,
        args=(await get_alienvault_phishing_feed(settings.feeds.alienvault_turkey),),
    )
    scheduler.add_job(
        bulk_insert_phishing_url,
        "interval",
        hours=1,
        args=(await get_alienvault_phishing_feed(settings.feeds.alienvault_domain),),
    )
    scheduler.add_job(
        bulk_insert_phishing_url,
        "interval",
        hours=1,
        args=(await get_alienvault_phishing_feed(settings.feeds.alienvault_url),),
    )
    scheduler.add_job(
        bulk_insert_phishing_url,
        "interval",
        hours=1,
        args=(await get_tweet_phishing_feed(settings.feeds.tweet_feed),),
    )
    scheduler.add_job(
        get_phishtank_feed,
        "interval",
        hours=1,
        args=(settings.feeds.phishtank_feed,),
    )

    scheduler.start()

    try:
        # Code that runs asynchronously forever.
        await asyncio.sleep(float("inf"))
    except:
        pass


if __name__ == "__main__":
    asyncio.run(main())
