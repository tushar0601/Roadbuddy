/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useParams } from "next/navigation";
import { useState } from "react";
import { API_BASE } from "@/lib/api";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

type Reason = "BLOCKED" | "WRONG_PARKING" | "EMERGENCY";

export default function PublicScanPage() {
  const { code } = useParams<{ code: string }>();

  const [reason, setReason] = useState<Reason>("BLOCKED");
  const [note, setNote] = useState("");
  const [done, setDone] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function submit() {
    setErr(null);
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE}/s/${code}/ping`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          reason,
          note: note || null,
        }),
      });

      if (!res.ok) {
        setErr(await res.text());
        return;
      }

      setDone(true);
    } catch (e: any) {
      setErr(e?.message || "Failed to notify owner");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-6">
      <Card className="w-full max-w-lg">
        <CardHeader>
          <CardTitle>Notify vehicle owner</CardTitle>
        </CardHeader>

        <CardContent className="space-y-4">
          {done ? (
            <div className="text-sm text-green-600">
              Owner notified successfully.
            </div>
          ) : (
            <>
              <div className="space-y-2">
                <Label>Reason</Label>

                <Select
                  value={reason}
                  onValueChange={(value: Reason) => setReason(value)}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select reason" />
                  </SelectTrigger>

                  <SelectContent>
                    <SelectItem value="BLOCKED">Blocked my vehicle</SelectItem>

                    <SelectItem value="WRONG_PARKING">Wrong parking</SelectItem>

                    <SelectItem value="EMERGENCY">Emergency</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <Label>Note (optional)</Label>

                <Textarea
                  value={note}
                  onChange={(e) => setNote(e.target.value)}
                  maxLength={300}
                  placeholder="Additional details (optional)"
                />
              </div>

              <Button onClick={submit} disabled={loading} className="w-full">
                {loading ? "Sending..." : "Notify owner"}
              </Button>

              {err && <div className="text-sm text-red-600">{err}</div>}
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
