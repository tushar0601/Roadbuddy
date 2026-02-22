import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div className="min-h-screen w-full bg-gradient-to-b from-zinc-50 to-white dark:from-zinc-950 dark:to-black">
      <header className="mx-auto flex max-w-6xl items-center justify-between p-6">
        <div className="flex items-center gap-2">
          <div className="h-10 w-10 rounded-2xl bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-semibold">
            RB
          </div>
          <div>
            <div className="font-semibold leading-none">RoadBuddy</div>
            <div className="text-xs text-muted-foreground">
              Parking pings without phone numbers
            </div>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <Button asChild variant="outline" className="rounded-xl">
            <Link href="/signin">Sign in</Link>
          </Button>
          <Button asChild className="rounded-xl">
            <Link href="/dashboard">Dashboard</Link>
          </Button>
        </div>
      </header>

      <main className="mx-auto max-w-6xl px-6 pb-16 pt-10">
        <div className="grid gap-10 md:grid-cols-2 md:items-center">
          <div className="space-y-5">
            <h1 className="text-4xl font-semibold tracking-tight md:text-5xl">
              A safer way to ask someone to move their vehicle.
            </h1>
            <p className="text-lg text-muted-foreground leading-8">
              RoadBuddy generates a QR sticker for your car/bike. Anyone can
              scan it to send you an in-app notification — without exposing your
              personal phone number.
            </p>

            <div className="flex flex-col gap-3 sm:flex-row">
              <Button asChild size="lg" className="rounded-xl">
                <Link href="/signin">Get started</Link>
              </Button>
              <Button
                asChild
                size="lg"
                variant="outline"
                className="rounded-xl"
              >
                <Link href="/dashboard">View dashboard</Link>
              </Button>
            </div>

            <div className="text-sm text-muted-foreground">
              Built for dense parking environments (hello, Delhi) where “blocked
              vehicle” happens daily.
            </div>
          </div>

          <div className="rounded-2xl border bg-white/60 p-6 shadow-sm backdrop-blur dark:bg-zinc-950/40">
            <div className="grid gap-4">
              <div className="rounded-xl border bg-background p-4">
                <div className="font-medium">1) Create a vehicle</div>
                <div className="text-sm text-muted-foreground mt-1">
                  Add label and optional plate last-4.
                </div>
              </div>
              <div className="rounded-xl border bg-background p-4">
                <div className="font-medium">2) Generate a QR sticker</div>
                <div className="text-sm text-muted-foreground mt-1">
                  QR links to{" "}
                  <span className="font-mono">/s/&lt;public_code&gt;</span>{" "}
                  (unguessable).
                </div>
              </div>
              <div className="rounded-xl border bg-background p-4">
                <div className="font-medium">3) Someone scans & pings you</div>
                <div className="text-sm text-muted-foreground mt-1">
                  Choose a reason (Blocked / Wrong parking / Emergency) +
                  optional note.
                </div>
              </div>
              <div className="rounded-xl border bg-background p-4">
                <div className="font-medium">4) You get notified</div>
                <div className="text-sm text-muted-foreground mt-1">
                  In-app notifications + audit trail (ping events).
                </div>
              </div>
            </div>

            <div className="mt-6 text-xs text-muted-foreground">
              Privacy-first by design. Abuse controls: reason validation, note
              length cap, IP hashing (rate limiting next).
            </div>
          </div>
        </div>

        <section className="mt-14 grid gap-6 md:grid-cols-3">
          <div className="rounded-2xl border bg-white/60 p-6 shadow-sm backdrop-blur dark:bg-zinc-950/40">
            <div className="text-sm font-medium">Privacy</div>
            <div className="mt-2 text-sm text-muted-foreground">
              No phone number on windshields. QR pings go to in-app
              notifications.
            </div>
          </div>
          <div className="rounded-2xl border bg-white/60 p-6 shadow-sm backdrop-blur dark:bg-zinc-950/40">
            <div className="text-sm font-medium">Security</div>
            <div className="mt-2 text-sm text-muted-foreground">
              Uses unguessable public codes (stickers). Tracks ping events for
              auditability.
            </div>
          </div>
          <div className="rounded-2xl border bg-white/60 p-6 shadow-sm backdrop-blur dark:bg-zinc-950/40">
            <div className="text-sm font-medium">Built to scale</div>
            <div className="mt-2 text-sm text-muted-foreground">
              FastAPI + Postgres + Alembic + Next.js + shadcn — clean
              architecture, ready for rate limiting & realtime.
            </div>
          </div>
        </section>

        <footer className="mt-16 border-t pt-6 text-sm text-muted-foreground">
          <div className="mx-auto max-w-6xl">
            RoadBuddy — QR-based parking notifications. Built with Supabase
            OAuth.
          </div>
        </footer>
      </main>
    </div>
  );
}
