"use client";

import type { Notification } from "@/lib/types";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

function formatTime(iso: string) {
  const d = new Date(iso);
  return d.toLocaleString();
}

export function NotificationsCard({
  notifications,
}: {
  notifications: Notification[];
}) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Notifications</CardTitle>
      </CardHeader>
      <CardContent className="space-y-3">
        {notifications.length === 0 ? (
          <div className="text-sm text-muted-foreground">
            No notifications yet.
          </div>
        ) : (
          <div className="space-y-3">
            {notifications.slice(0, 30).map((n) => (
              <div key={n.id} className="rounded-md border p-3">
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <div className="font-medium">{n.title}</div>
                    <div className="text-sm text-muted-foreground">
                      {n.body}
                    </div>
                  </div>
                  <div className="text-xs text-muted-foreground whitespace-nowrap">
                    {formatTime(n.created_at)}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
